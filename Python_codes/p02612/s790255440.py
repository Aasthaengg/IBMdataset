N = int(input())
count = int(N/1000)
if N%1000 == 0:
    print(0)
else:
    print((count+1)*1000-N)