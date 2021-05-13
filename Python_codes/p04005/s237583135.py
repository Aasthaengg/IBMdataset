ABC=list(map(int,input().split()))
ABC.sort()
temp=ABC[2]//2
print(ABC[0]*ABC[1]*(ABC[2]-temp)-ABC[0]*ABC[1]*temp)
