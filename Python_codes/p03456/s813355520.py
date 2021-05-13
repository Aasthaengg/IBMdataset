a, b = input().split()
c = int(a + b)

if (c**0.5).is_integer():
    print('Yes' , flush=True)
else:
    print('No' , flush=True)
