k, x = map(int, input().split())
if k == 1:
    print(x)
    exit()
#print(7-3+1)~print(7+3-1)
for i in range(x-k+1, k+x):
    print(i, end=" ")
print()