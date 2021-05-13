def kitaichi(x):
    return x * (x+1) / (2 * x)

def main():
    n, k = map(int, input().split())
    inlis = tuple(map(int, input().split()))
    kitalis = list(map(kitaichi, inlis))
    kitadic = {}
    kitadic[0] = kitalis[0] 
    for i in range(1, n):
        kitadic[i] = kitadic[i-1] + kitalis[i]
       
    tmp = 0
    if n == k:
        print(kitadic[n-1])
    else:
        for i in range(n - k):
            atai = kitadic[i+k] - kitadic[i]
            if tmp < atai:
                tmp = atai
        print(tmp)
        exit()



    
if __name__ == "__main__":
    main()
