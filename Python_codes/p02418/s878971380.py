def main():

    sentence = input()
    phrase = input()
    count = 0
    for _ in range(len(sentence)):
        if phrase in sentence:
            count =  1
            break
        else:
            sentence = sentence[1:] + sentence[0]
    
    if count == 1:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
