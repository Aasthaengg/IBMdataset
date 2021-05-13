#13
import sys

h,w = map(int,input().split())
s = []
s.append(list("."*(w+2)))
for i in range(h):
    a = "."+input()+"."
    s.append(list(a))
s.append(list("."*(w+2)))


for i in range(1,h+1):
    for j in range(1,w+1):
        check = 0
        if s[i][j] == "#":
            for m in range(i-1,i+2,2):
                if s[m][j] == "#":
                    check +=1
                    break
            if check == 0:
                for n in range(j-1,j+2,2):
                    if s[i][n] == "#":
                        check += 1
                        break
            if check == 0:
                print("No")
                sys.exit()
            
            
            
print("Yes")