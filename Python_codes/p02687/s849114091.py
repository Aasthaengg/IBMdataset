import math  # noqa: F401
from typing import Dict, List, Optional, Tuple, Union  # noqa: F401


def main(S: str):
    print(["ABC", "ARC"][S == "ABC"])


if __name__ == "__main__":
    S = input()
    main(S)
