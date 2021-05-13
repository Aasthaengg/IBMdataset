def main():
    s = input()
    cr = 0
    cp = 0
    score = 0
    for c in s:
        if c == 'g':
            if cr > cp:
                score += 1
                cp += 1
            else:
                cr += 1
        else:
            if cr > cp:
                cp += 1
            else:
                cr += 1
                score -= 1
    print(score)
    

if __name__ == '__main__':
    main()