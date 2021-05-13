k = int(raw_input())
lis = raw_input().split()

for i in range(1, k):
    print str(lis[k-i]),

print lis[0]