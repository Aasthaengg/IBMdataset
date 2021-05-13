n = int(input())
d = sorted(list(map(int,input().split())),reverse=True)
m = int(input())
t = sorted(list(map(int,input().split())))

for i in t:
    while d:
        tmp_d = d.pop()
        if i == tmp_d:
            break
    else:
        print("NO")
        exit()
print("YES")


