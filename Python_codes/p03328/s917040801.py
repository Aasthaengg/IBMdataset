
def main():
    a,b = map(int, input().split())
    sum = 0
    
    for height in range(1,1000):
        sum += height
        if b-a == height:
            print(sum-b)
            break;
        
if __name__ == "__main__":
    main()