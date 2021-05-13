    
def main():
    x, y = map(int, input().split(" "))
    leg_num = 4*x
    for i in range(x+1):
        if leg_num - i*2 == y:
            print("Yes")
            return
    print("No")

if __name__ == "__main__":
    main()