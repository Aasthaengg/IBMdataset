x, k, d = map(int, input().split())
x = abs(x)
if x > k*d:
    print(x-k*d)
else:
    p = x//d
    c = k-p
    if p == 0 or p==1:
          for i in range(1,k+1):
            p2 = x-i*d
            c = k-i
            if p2 <= 0:
                if c%2 != 0:
                    print(abs(d+p2))
                    break
                elif c%2 == 0:
                    print(abs(p2))
                    break
    elif (c%2 == 0):
        print(abs(x-p*d))
    else:
        print(abs(d-abs(x-p*d)))