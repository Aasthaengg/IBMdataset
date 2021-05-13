def q1():
    N = input()
    ans = 'No'
    for i in range(10):
        s = '{0}{0}{0}'.format(i)
        if s in N:
            return 'Yes'

    return ans


if __name__ == "__main__":
    print(q1())
