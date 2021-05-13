import sys
input = sys.stdin.buffer.readline

def main():
    N = int(input())
    food = []
    sc = 0
    for _ in range(N):
        a,b = map(int,input().split())
        sc -= b
        food.append(a+b)
    
    food.sort(reverse= True)
    tf = sum(food[::2])
    print(tf+sc)

if __name__ == "__main__":
    main()
