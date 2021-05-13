def main():
    A, B, C = map(int, input().split())
    Task = sorted([A, B, C])
    print(Task[-1]-Task[0])
if __name__ == "__main__":
    main()