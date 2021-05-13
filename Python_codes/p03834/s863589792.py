def resolve():
    s = input()
    print(s.translate(str.maketrans({",": " "})))

resolve()