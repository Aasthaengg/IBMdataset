n=int(input())
alp=["z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y"]
ans=""
while n>0:
    ans=alp[n%26]+ans
    n=(n-1)//26

print(ans)
