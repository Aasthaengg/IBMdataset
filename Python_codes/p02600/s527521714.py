n=int(input())
for i in range(8):
    if 1800-200*i<=n<2000-100*i:
        print(i+1)
        break