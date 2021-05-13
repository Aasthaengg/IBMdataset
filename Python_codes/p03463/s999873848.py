N, A, B = map(int, input().split())
if (A % 2 == 0) ^ (B % 2 == 0): 
        print("Borys")
else:
        print("Alice")