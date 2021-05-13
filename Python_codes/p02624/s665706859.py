n = int(input())
cnts = [k*(n//k)*((n//k)+1)//2 for k in range(1,n//2+1)]
print(sum(cnts)+ ((n//2+1)+n)*(n-(n//2+1)+1)//2)