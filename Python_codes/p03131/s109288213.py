K,A,B=map(int,input().split())
b_count=1

if B-A<=2:
    b_count+=K
else:
    b_chenge_count=max(0,int((K-(A-1))/2))
    b_count+=b_chenge_count*(B-A)+(A-1)+(K-(A-1)-b_chenge_count*2)

print(b_count)