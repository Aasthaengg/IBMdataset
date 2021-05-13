
def main():

    N = int(input())
    s = input()
    count = 0
    for c in s:
        if c == "R":
            count += 1
        else:
            count -= 1
    if count > 0: return "Yes"
    return "No"

if __name__ == '__main__':
    print(main())