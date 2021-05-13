print(len(list(filter(lambda x: x == 0, map(lambda x, y: True if x == y else False, list("CODEFESTIVAL2016"), list(input()))))))
