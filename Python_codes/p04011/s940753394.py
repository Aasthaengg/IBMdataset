# A - 高橋君とホテルイージー
def main():
    n = int(input())
    k = int(input())
    x = int(input())
    y = int(input())
    cost = 0

    for i in range(1, n+1):
        if i <= k:
            cost += x
        else:
            cost += y
    else:
        print(cost)
        
    
if __name__ ==  "__main__":
    main()