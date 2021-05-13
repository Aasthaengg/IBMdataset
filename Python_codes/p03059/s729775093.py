line = input()
A,B,T = [int(n) for n in line.split()]
print(int(B*((T+0.5)//A)))