n = input()
l = input()
ans = True
#print(n[0])
#print(n[])
for i in range(len(n)):
    if i ==0:
        if n[0] == l[-1]:
            continue
        else :
            ans = False
            break
        
    elif n[i] == l[-i-1]:
        continue
    else :
        ans = False
        break
if ans:
    print("YES")
else:
    print("NO")
