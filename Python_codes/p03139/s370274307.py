N,A,B = map(int,input().split())
A_N = N - A
B_N = N - B
print(min(A,B) , max(0,A + B - N))