if __name__ == "__main__":
    n = int(input())
    array = [int(i) for i in input().split()]
    print("%d %d %d"%(min(array),max(array),sum(array)))