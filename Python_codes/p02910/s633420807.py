import sys


# input = sys.stdin.readline

def main():
    S = input()
    count =1
    for i in S:
        if count %2==1 and i =="L":
            print("No")
            exit()
        elif count%2 ==0 and i =="R":
            print("No")
            exit()

        count+=1
    print("Yes")





if __name__ == "__main__":
    main()