print(
    "Yes"
    if "CF" in "".join([s if s == "C" or s == "F" else "" for s in input()])
    else "No"
)
