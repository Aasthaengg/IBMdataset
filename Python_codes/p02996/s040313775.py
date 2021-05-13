def main():
    N = int(input())
    works = []
    for i in range(N):
        A, B = map(int, input().split())
        works.append((A, B))
    
    works.sort(key=lambda x: x[1])

    time = 0
    for i in range(N):
        a, b = works[i]
        time += a
        if time > b:
            print('No')
            return
    print('Yes')

if __name__ == "__main__":
    main()
