O = input()
E = input()
ans = ""
for i in range(len(O+E)) :
    if i % 2 == 0:
        ans += O[i//2]
    else :
        ans += E[(i+1)//2-1]
print(ans)