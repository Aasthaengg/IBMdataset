import math

def main():
    A, B, K = map(int, input().split())
    
    c_list = []
    
    for i in range(1, min(A, B)+1):
        if A%i==0 and B%i==0:
            c_list.append(i)
    c_list.reverse()
    print(c_list[K-1])
main()