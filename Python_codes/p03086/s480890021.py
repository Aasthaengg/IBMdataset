if __name__ == "__main__":
    S = input()
    word_arr = ["A","T","G","C"]
    max_count,count = 0,0
    for c in S:
        if c in word_arr:
            count += 1
        else:
            max_count = max(count,max_count)
            count = 0
    max_count = max(count,max_count)
    print(max_count)