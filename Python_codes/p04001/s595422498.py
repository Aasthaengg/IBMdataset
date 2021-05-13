from collections import deque

def main():
    N = list(input())
    Nq = deque(N)
    anstmp = []
    ans = 0

    for bit in range(2**(len(N) - 1)):
        for i in range(len(N)):
            anstmp.append(str(Nq.popleft()))
            if ((bit >> i) & 1): 
                anstmp.append("+")
        # print("".join(anstmp))
        ans += eval("".join(anstmp))

        Nq = deque(N) 
        anstmp = []  

    print(ans)
    
        

if __name__ == "__main__":
    main()
