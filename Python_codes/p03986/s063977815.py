def main(X):
    cntS = 0; cntT = 0
    for x in X:
        if x == 'T' and cntS == 0:
            cntT += 1
        elif x == 'S':
            cntS += 1
        elif x == 'T' and cntS > 0:
            cntS -= 1
        else:
            pass
    return cntS + cntT
    
if __name__ == "__main__":
    X = list(input())
    ans = main(X)
    print(ans)
