import numpy as np

def main():
    H,W = map(int,input().split())
    use = np.zeros((H,W),dtype=int)
    for i in range(H):
        s = input()
        for j,st in enumerate(s):
            if st == ".":
                use[i][j] = 10**10
            else:
                use[i][j] = 0
    
    for i in range(1,H):
        use[i,:] = np.minimum(use[i,:],use[i-1,:]+1)
    for i in reversed(range(H-1)):
        use[i,:] = np.minimum(use[i,:],use[i+1,:]+1)
    for j in range(1,W):
        use[:,j] = np.minimum(use[:,j],use[:,j-1]+1)
    for j in reversed(range(W-1)):
        use[:,j] = np.minimum(use[:,j],use[:,j+1]+1)
    
    print(np.max(use))

if __name__ == "__main__":
    main()
