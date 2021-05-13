H,W=map(int,input().split())
zu=["."*(W+2)]

for i in range(H):
  zu.append("."+input()+".")

zu.append(zu[0])
#print(zu)

for h in range(1,H+2):
    for w in range(1,W+2):
        if zu[h][w]=="#":
          if zu[h-1][w]==".":
            if zu[h][w-1]==".":
              if zu[h+1][w]==".":
                if zu[h][w+1]==".":
                  print("No")
                  break
   
    else:
        continue
    break

else:
  print("Yes")
  
#if zu[h-1][w]=="." and zu[h][w-1]=="." and zu[h+1][w]=="." and zu[h][w+1]==".":