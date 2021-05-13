HW=list(map(int,input().split()))
hw=list(map(int,input().split()))
ans=HW[0]*HW[1]
b=hw[0]*HW[1]+hw[1]*HW[0]-hw[0]*hw[1]
ans-=b
print(ans)
