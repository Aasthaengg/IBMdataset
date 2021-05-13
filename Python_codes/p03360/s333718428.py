a,b,c=map(int,input().split())
k=int(input())

kazu=[a,b,c]
kazu.sort()
#print(kazu)
print(kazu[0]+kazu[1]+kazu[2]*2**k)