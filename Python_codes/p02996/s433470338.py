def main():
    n=int(input())
    task=[tuple(map(int,input().split())) for _ in range(n)]
    task.sort(key=lambda x: x[1])
    current = 0
    for a,b in task:
        current += a
        if current > b:
            break
    else:
        print("Yes")
        return
    print("No")
    

if __name__ == "__main__":
    main()