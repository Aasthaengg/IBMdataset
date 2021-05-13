def main():
    s = input()
    t = input()
    ans = 'No'
    s2 = s * 2
    for i in range(len(s2)):
        if t == s2[i:i + len(s)]:
            ans = 'Yes'
            break
    print(ans)



if __name__ == '__main__':
    main()