s = input()
w=0
l=0
for x in s:
    if x is 'o':
        w+=1
    else:
        l+=1
if w+15-l-w>=8:
    print("YES")
else:
    print("NO")