n=int(input())
for i in range(int(n/1.08),int((n+1)/1.08)+1):
    if n/1.08<=i<(n+1)/1.08:
        print(i)
        import sys
        sys.exit()
else:
    print(':(')