# row = [int(x) for x in input().rstrip().split(" ")]
# n = int(input().rstrip())
# s = input().rstrip()

def resolve():
    import sys
    input = sys.stdin.readline

    n = int(input().rstrip())

    data = {}

    for i in range(n):
        row = [x for x in input().rstrip().split(" ")]
        s = row[0]
        p = int(row[1])

        if s not in data.keys():
            data[s] = {}

        data[s][p] = i+1

    for city, res in sorted(data.items()):
        for point, num in sorted(res.items(), reverse=True):
            print(num)





if __name__ == "__main__":
    resolve()
