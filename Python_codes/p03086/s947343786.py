def main():
    s = input()
    max_length = 0
    cur_length = 0
    for i, si in enumerate(s):
        if si in ["A", "T", "G", "C"]:
            cur_length+=1
        else:
            if max_length<cur_length:
                max_length = cur_length
            cur_length = 0

    if max_length<cur_length:
        max_length = cur_length
    print(max_length)

if __name__=="__main__":
    main()

