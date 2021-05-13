ABC = [int(e) for e in input().split()]

min_ABC = 10**9

for i in range(3):
    if ABC[i]%2==0:
        print(0)
        break
else:
    ABC.sort(reverse=False)
    print(ABC[0]*ABC[1]*(ABC[2]-ABC[2]//2*2))