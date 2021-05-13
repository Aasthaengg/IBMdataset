def main():
    owner_num = 753
    s = input()
    min_diff = int(s[0:3])
    for i in range(3,len(s)+1):
        runrun_num = int(s[(i-3):i])
        if abs(owner_num - runrun_num) < abs(owner_num - min_diff):
            min_diff = runrun_num
    print(abs(owner_num - min_diff))



if __name__ == '__main__':
    main()
