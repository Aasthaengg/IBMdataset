N,S,z=int(input()),input(),0
for i in range(1,N):a,b=S[:i],S[i:];z=max(z,len([0 for j in range(97,123)if chr(j)in a and chr(j)in b]))
print(z)