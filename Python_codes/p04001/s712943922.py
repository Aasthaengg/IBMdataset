def sum(list, index):
    if (len(list) > 1):
        d = len(list[:-1]) - 1
        return (sum(list[:-1], 0) + list[-1] * 10**index * 2**d ) + (sum(list[:-1], index + 1 ) + list[-1] * 10**index * 2**d)
    else:
        return (list[-1] * 10**index)

def resolve():
    s = list(map(int,input()))
    print(sum(s,0))


if __name__ == "__main__":
    resolve()