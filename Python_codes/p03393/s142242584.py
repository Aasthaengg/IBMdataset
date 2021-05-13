from collections import Counter
s=input()

# sが26文字未満のとき
a_l=[chr(i) for i in range(ord("a"),ord("z")+1)]
if len(s)<26:print(s+sorted(set(a_l)-set(s))[0]);exit()

# sが26文字のとき
for i,x in enumerate(s[::-1]):
    l=[chr(i) for i in range(ord("a"),ord("z")+1) if ord(x)<i]
    for y in l:
        if Counter(s[:26-i-1]+y).most_common(1)[0][1]==1:
            print(s[:26-i-1]+y)
            exit()

print(-1)