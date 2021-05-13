num=list(map(int,input().split()))
print("Possible" if sum(num)%3==0 or num[0]%3==0 or num[1]%3==0 else "Impossible")