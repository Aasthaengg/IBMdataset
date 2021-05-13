s = input()
a = ""
b = ""
if len(s)%2==0:
    a = s[:(len(s)//2)]
    b = s[(len(s)//2):][::-1]
else:
    a = s[:(len(s)//2)]
    b = s[(len(s)//2)+1:][::-1]
cnt = 0
for a_, b_ in zip(a,b):
    if not a_ == b_:
        cnt += 1
print(cnt)